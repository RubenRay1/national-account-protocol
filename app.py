import boto3
import json
from flask import Flask, render_template, request, jsonify
from boto3.dynamodb.conditions import Attr
import os

app = Flask(__name__)

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('bms-national-account-protocol-ddb')

def scan_table():
    """Scan entire DynamoDB table and return all items"""
    try:
        response = table.scan()
        items = response['Items']
        
        # Handle pagination
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response['Items'])
        
        return items
    except Exception as e:
        print(f"Error scanning table: {e}")
        return []

def search_items(query):
    """Search items containing the query string"""
    if not query:
        return scan_table()
    
    try:
        # Get all items first (for small datasets)
        all_items = scan_table()
        
        # Filter items that contain the search query in any field
        filtered_items = []
        query_lower = query.lower()
        
        for item in all_items:
            for key, value in item.items():
                if isinstance(value, str) and query_lower in value.lower():
                    filtered_items.append(item)
                    break
        
        return filtered_items
    except Exception as e:
        print(f"Error searching items: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    query = request.args.get('search', '')
    items = search_items(query)
    return jsonify(items)

@app.route('/api/stats')
def get_stats():
    items = scan_table()
    return jsonify({'total_records': len(items)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
