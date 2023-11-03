import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import pdfkit

# Input the URL from the user
url = input("Enter the URL: ")

# Set the JMeter test plan file and URL parameter
jmeter_test_plan = 'my_test.jmx'
jmeter_url_parameter = f'-Jurl={url}'

# Run JMeter using subprocess to generate the CSV result file
try:
    # Replace 'jmeter' with the path to your JMeter executable
    subprocess.run(['jmeter', '-n', '-t', jmeter_test_plan, jmeter_url_parameter])
except FileNotFoundError:
    print("JMeter not found. Please make sure JMeter is installed and added to your system's PATH.")
except Exception as e:
    print(f"An error occurred: {e}")

# Read the CSV result file using Pandas
result_file = 'results.csv'  # Update this with the path to your JMeter CSV result file
df = pd.read_csv(result_file)

# Calculate the average, highest, and lowest response times
average_response_time = df['elapsed'].mean()
highest_response_time = df['elapsed'].max()
lowest_response_time = df['elapsed'].min()

# Display the results
print("JMeter Test Results:")
print(df)
print(f"Average Response Time: {average_response_time} ms")
print(f"Highest Response Time: {highest_response_time} ms")
print(f"Lowest Response Time: {lowest_response_time} ms")

# Create a table from the DataFrame and save it to a temporary HTML file
table_html = df.to_html()

# Use pdfkit to convert the HTML to a PDF file
pdfkit.from_file('temp_table.html', 'output.pdf')