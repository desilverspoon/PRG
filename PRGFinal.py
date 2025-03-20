import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import matplotlib.pyplot as plt  # Import matplotlib for graph generation
import time
import schedule

# Print the title
print("\n" + "="*75)
print(" " * 10 + "Premier Rating Grabber v1.0 by SilverSpoon")
print("="*75 + "\n")

# Define the default file paths
current_directory = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory
csv_file = os.path.join(current_directory, "Ratings.csv")  # Save the CSV file in the same directory as the script
text_file = os.path.join(current_directory, "overlay_data.txt")  # Text file for Streamlabs overlay
graph_file = os.path.join(current_directory, "graph.png")  # File to save the graph image

# Ensure the directory exists
os.makedirs(os.path.dirname(csv_file), exist_ok=True)

# Initialize the CSV file with headers if it doesn't exist
try:
    with open(csv_file, 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Rating'])  # Headers
except FileExistsError:
    pass  # File already exists, no need to rewrite headers

# Function to generate a graph from the CSV data
def generate_graph():
    try:
        print("Generating graph...")
        # Read the data from the CSV file
        dates = []
        ratings = []
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dates.append(datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S'))
                ratings.append(int(row['Rating'].replace(',', '')))  # Convert rating to integer

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(dates, ratings, marker='o', linestyle='-', color='b', label='Player Rating')
        plt.title('Player Rating Over Time')
        plt.xlabel('Date')
        plt.ylabel('Rating')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        # Save the graph as an image
        plt.savefig(graph_file)
        plt.close()
        print(f"Graph saved to {graph_file}")
    except Exception as e:
        print("Error generating the graph:", e)

# Function to extract the rating and save it to the CSV and text file
def extract_and_save_data():
    print("Starting extract_and_save_data...")
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-direct-composition")
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--headless")  # Uncomment to run in headless mode

    # Specify the path to the ChromeDriver
    service = Service('C:/chromedriver/chromedriver.exe')  # Update this path

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # URL of the player profile
        url = 'https://leetify.com/app/profile/YOUR_ID_HERE'
        print(f"Navigating to URL: {url}")
        driver.get(url)

        # Wait for the label-large element to load
        try:
            large_label = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='rank-and-name']//div[contains(@class, 'cs-rating')]//span[contains(@class, 'label-large')]"))
            ).text
        except Exception as e:
            print("Error Scraping Rating: Check your url is correct.", e)
            return

        # Wait for the label-small element to load
        try:
            small_label = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='rank-and-name']//div[contains(@class, 'cs-rating')]//span[contains(@class, 'label-small')]"))
            ).text
        except Exception as e:
            print("Error Scraping Rating: Check your url is correct.", e)
            return

        # Combine the values
        full_rating = large_label + small_label
        print(f"Extracted Rating: {full_rating}")

        # Save to CSV
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_date, full_rating])

        # Save to text file for Streamlabs overlay
        with open(text_file, 'w') as file:
            file.write(f"Player Rating: {full_rating}")

        print(f"Data saved: {current_date}, {full_rating}")

        # Generate the graph
        generate_graph()
    except Exception as e:
        print("Error in extract_and_save_data:", e)
    finally:
        # Close the browser
        driver.quit()

# Schedule the function to run every 30 minutes
print("Scheduling task to run every 30 minutes...")
schedule.every(30).minutes.do(lambda: print("Task scheduled: extract_and_save_data"))

# Run the task immediately on startup
extract_and_save_data()

# Keep the script running
try:
    while True:
        print("Running scheduled tasks...")
        schedule.run_pending()
        time.sleep(60)  # Sleep for 1 second to avoid high CPU usage
except KeyboardInterrupt:
    print("Script stopped by user.")
schedule.every(30).minutes.do(extract_and_save_data)
