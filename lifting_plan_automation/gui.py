

import streamlit as st
import pandas as pd
import os
import main
import excel_io
import tempfile

def streamlit_app():
    st.title("Lifting Plan Automation")

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
                        output_excel_path, output_dxf_path = main.main(temp_excel_path, output_dir=temp_dir)

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
