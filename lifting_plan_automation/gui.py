import streamlit as st
import pandas as pd
import os
import tempfile
from lifting_plan_automation import main, excel_io

def streamlit_app():
    st.title("Lifting Plan Automation")

    st.write("Enter the lifting parameters or upload an Excel file.")

    load_weight = st.number_input("Load Weight (tons)", min_value=0.0, value=10.0, step=0.5)
    sling_angle = st.number_input("Sling Angle (degrees)", min_value=0.0, max_value=90.0, value=60.0, step=1.0)
    num_slings = st.number_input("Number of Slings", min_value=1, value=4, step=1)
    crane_capacity = st.number_input("Crane Capacity (tons)", min_value=0.0, value=20.0, step=1.0)
    sling_wll = st.number_input("Sling WLL (tons each)", min_value=0.0, value=5.0, step=0.5)

    st.write("Upload your lifting plan Excel file to get started.")

    uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

    if uploaded_file is not None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_excel_path = os.path.join(temp_dir, uploaded_file.name)
            with open(temp_excel_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.write("### Uploaded Lifting Parameters")
            df = pd.read_excel(uploaded_file)
            st.dataframe(df)

            if st.button("Generate Lifting Plan"):
                with st.spinner("Generating lifting plan..."):
                    try:
                        output_excel_path, output_dxf_path = main.main(
                            filepath=temp_excel_path,
                            output_dir=temp_dir,
                            load_weight=load_weight,
                            sling_angle=sling_angle,
                            num_slings=num_slings,
                            crane_capacity=crane_capacity,
                            sling_swl=sling_wll
                        )

                        st.success("Lifting plan generated successfully!")

                        st.write("### Calculated Results")
                        results_df = pd.read_excel(output_excel_path)
                        st.dataframe(results_df)

                        with open(output_dxf_path, "rb") as f:
                            st.download_button(
                                label="Download DXF File",
                                data=f,
                                file_name="lifting_plan.dxf",
                                mime="application/dxf"
                            )
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
    else:
        if st.button("Generate Lifting Plan from Inputs"):
            with st.spinner("Generating lifting plan..."):
                try:
                    with tempfile.TemporaryDirectory() as temp_dir:
                        # Create a dummy excel file path
                        dummy_excel_path = os.path.join(temp_dir, "lifting_plan.xlsx")
                        # We need to create a dummy excel file for main to work
                        from openpyxl import Workbook
                        wb = Workbook()
                        ws = wb.active
                        ws.title = "LiftingPlan"
                        # Add headers
                        ws.append(["Parameter", "Value"])
                        # Add some dummy values, they will be overwritten
                        ws.append(["Load Weight", 0])
                        ws.append(["Load Length", 10]) # dummy value
                        ws.append(["Load Width", 2]) # dummy value
                        ws.append(["Number of Slings", 0])
                        ws.append(["Sling Length", 0])
                        ws.append(["Sling SWL", 0])
                        ws.append(["Shackle SWL", 5]) # dummy value
                        ws.append(["Hook Weight", 1]) # dummy value
                        ws.append(["Crane Capacity", 0])
                        wb.save(dummy_excel_path)


                        output_excel_path, output_dxf_path = main.main(
                            filepath=dummy_excel_path,
                            output_dir=temp_dir,
                            load_weight=load_weight,
                            sling_angle=sling_angle,
                            num_slings=num_slings,
                            crane_capacity=crane_capacity,
                            sling_swl=sling_wll
                        )

                        st.success("Lifting plan generated successfully!")

                        st.write("### Calculated Results")
                        results_df = pd.read_excel(output_excel_path)
                        st.dataframe(results_df)

                        with open(output_dxf_path, "rb") as f:
                            st.download_button(
                                label="Download DXF File",
                                data=f,
                                file_name="lifting_plan.dxf",
                                mime="application/dxf"
                            )
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    streamlit_app()
