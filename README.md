**Installation Guide**

1. Install Python
Make sure you have Python installed on your system. You can download and install the latest version of Python from the official Python website: https://www.python.org/downloads/

2. Install OpenCV
OpenCV is a computer vision library used in the provided code. You can install it using pip, the Python package installer, by running the following command in your terminal or command prompt:
*pip install opencv-python*


3. Install NumPy
NumPy is a fundamental package for scientific computing with Python. It is a dependency for OpenCV. You can install it using pip with the following command:
*pip install numpy*


4. Install BM3D
BM3D is a denoising algorithm used in the code. You can install it using pip with the following command:
*pip install bm3d*


5. Download the Code
Download the code files from the source where you obtained this README.md file. Extract the contents of the zip file to a directory of your choice.

6. Run the Code
To run the code, use the following command-line format:

*python your_script.py -F path/to/your/image.jpg -S s -st 1.0 -O outputfilename*

Replace your_script.py with the actual filename of the script you want to execute. Specify the input image file path using -F, select the style using -S (s=starry_night, t=the_wave, l=la_muse), and set the denoising strength using -st.

Make sure you have the necessary permissions to read and write files in the specified directories.

That's it! You should now have everything set up to run the code successfully.

Note: The above instructions assume you are using a Unix-like system or Windows command prompt. If you are using a different environment or package manager, please adjust the installation commands accordingly.

If you encounter any issues or have any questions, feel free to reach out for assistance.

Enjoy using the code!