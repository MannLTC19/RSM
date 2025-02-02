import requests
import base64
import time

API_KEY = '5e28d0fd12d4b881c0f32993e0d44e51997fbb16bf02cb9908294c5f833f9cc7'

def scan_url(url):
    headers = {
        'x-apikey': API_KEY,
    }
    data = {
        'url': url
    }
    try:
        # Submit URL for scanning
        response = requests.post('https://www.virustotal.com/api/v3/urls', data=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            # Extract the ID from the response
            analysis_id = result.get('data', {}).get('id', '')
            
            # Wait for a few seconds to allow analysis to complete
            time.sleep(3)
            
            # Get the analysis results
            analysis_response = requests.get(
                f'https://www.virustotal.com/api/v3/analyses/{analysis_id}',
                headers=headers
            )
            
            if analysis_response.status_code == 200:
                return analysis_response.json()
            
    except Exception as e:
        print(f"Error scanning URL: {str(e)}")
        return None
    
    return None

def get_url_report(scan_id):
    headers = {
        'x-apikey': API_KEY,
    }
    try:
        response = requests.get(f'https://www.virustotal.com/api/v3/analyses/{scan_id}', headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error getting report: {str(e)}")
        return None
    return None