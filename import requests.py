import requests
import csv

def download_and_convert_to_csv(url, output_filename):
  """Downloads text content from a URL and saves it as a CSV file.

  Args:
      url: The URL of the text file (string).
      output_filename: The name of the output CSV file (string).
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    # Check if the downloaded content is valid CSV format
    lines = response.text.splitlines()
    if not lines:
      raise ValueError("Downloaded content is empty")
    if all(line.count(',') == len(lines[0].split(',')) - 1 for line in lines[1:]):
      # All lines have the same number of commas, assuming CSV format
      with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([line.split(',') for line in lines])
      print(f"Downloaded and converted '{url}' to CSV file '{output_filename}'.")
    else:
      print(f"Downloaded content from '{url}' may not be valid CSV format. Not saving as CSV.")
  except requests.exceptions.RequestException as e:
    print(f"Error downloading from '{url}': {e}")

# Example usage: Using the provided URL
url = 'https://www2.census.gov/econ/bps/County/co0001c.txt'
output_filename = 'project_1.csv'  # Replace with your desired filename
download_and_convert_to_csv(url, output_filename)