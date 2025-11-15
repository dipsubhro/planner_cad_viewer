
# Lifting Plan Automation

This project is a Python-based automation tool for generating lifting plans. It uses a Streamlit web app to allow users to upload an Excel file with lifting parameters, and it will generate a DXF drawing of the lifting arrangement.

## Features

- User-friendly web interface powered by Streamlit.
- Reads lifting parameters from a user-uploaded Excel file.
- Calculates sling tension, sling angles, center of gravity, and crane utilization.
- Performs safety checks against SWL values.
- Automatically generates a DXF drawing of the lifting plan.
- Provides a download link for the generated DXF file.

## Prerequisites

- Python 3
- `openpyxl` library (`pip install openpyxl`)
- `ezdxf` library (`pip install ezdxf`)
- `streamlit` library (`pip install streamlit`)
- `pandas` library (`pip install pandas`)

## How to Use

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Streamlit App:**
    ```bash
    streamlit run lifting_plan_automation/streamlit_app.py
    ```

3.  **Open the Web App:**
    - A new tab will open in your web browser with the Streamlit application.

4.  **Upload Your Excel File:**
    - Create an Excel file with your lifting parameters. You can use the following structure as a template:

| Parameter                 | Value        | Unit    |
| :--------------------------|:-------------|:--------|
| **Load Details**              |              |         |
| Load Description          | Example Load |         |
| Load Weight               | 10000        | kg      |
| Load Length               | 6            | m       |
| Load Width                | 2.5          | m       |
| Load Height               | 2            | m       |
| **Lifting Gear**              |              |         |
| Number of Slings          | 4            |         |
| Sling Length              | 5            | m       |
| Sling SWL                 | 5000         | kg      |
| Shackle SWL               | 6000         | kg      |
| **Crane Details**             |              |         |
| Crane ID                  | CR-01        |         |
| Crane Capacity            | 25000        | kg      |
| Hook Weight               | 500          | kg      |
| **Rigging Arrangement**       |              |         |
| Sling Attachment Point X1 | -2           | m       |
| Sling Attachment Point Y1 | 1            | m       |
| Sling Attachment Point X2 | 2            | m       |
| Sling Attachment Point Y2 | 1            | m       |
| Sling Attachment Point X3 | -2           | m       |
| Sling Attachment Point Y3 | -1           | m       |
| Sling Attachment Point X4 | 2            | m       |
| Sling Attachment Point Y4 | -1           | m       |

    - Drag and drop your Excel file into the file uploader on the web app.

5.  **Generate the Lifting Plan:**
    - Click the "Generate Lifting Plan" button to perform the calculations and create the DXF drawing.

6.  **Download the DXF File:**
    - A "Download DXF File" button will appear, allowing you to save the generated `lifting_plan.dxf` file.

## Project Structure

- `lifting_plan_automation/`: Directory containing the Python source code.
    - `main.py`: The main application script.
    - `excel_io.py`: Module for reading data from the Excel file.
    - `calculations.py`: Module for performing engineering calculations.
    - `drawing.py`: Module for generating the DXF drawing.
    - `streamlit_app.py`: The Streamlit web application.
- `requirements.txt`: A file with the project's dependencies.
