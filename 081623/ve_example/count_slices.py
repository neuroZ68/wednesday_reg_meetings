import pandas as pd
import nibabel as nib

def count_slices(file_path):
    # Load the nifti image
    roi_img = nib.load(file_path)

    # Get the data as a numpy array
    roi_data = roi_img.get_fdata()

    # Create a DataFrame from the numpy array
    roi_df = pd.DataFrame(roi_data.reshape(-1, roi_data.shape[-1]))

    # Convert DataFrame to a single series
    roi_series = roi_df.values.flatten()

    # Find unique values
    unique_values = pd.Series(roi_series).unique()

    # Initialize a dictionary to hold the counts
    counts = {}

    # Iterate over the unique values
    for val in unique_values:
        # Initialize a counter for each unique value
        counts[val] = 0

        # Iterate over each slice
        for i in range(roi_data.shape[2]):
            # If the value is present in the slice, increment the counter
            if val in roi_data[:, :, i]:
                counts[val] += 1

    # Convert the dictionary to a DataFrame
    counts_df = pd.DataFrame(list(counts.items()), columns=['ROI', 'Number of Slices'])
    
    return counts_df