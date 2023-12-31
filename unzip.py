import zipfile

# Function to report progress with percentage
def extract_with_progress(zip_file_path, extract_to_path):
    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Get the list of file names in the zip
        total_files = len(zip_ref.namelist())
        print(f"Total files and directories to extract: {total_files}")

        # Loop through each file
        for i, file in enumerate(zip_ref.namelist(), 1):
            # Extract the file
            zip_ref.extract(file, extract_to_path)
            # Calculate the percentage completed
            percentage = (i / total_files) * 100
            # Print the progress with percentage
            print(f"Extracting file {i} of {total_files} ({percentage:.2f}%)", end="\r", flush=True)

        print("\nUnzipping completed!")


