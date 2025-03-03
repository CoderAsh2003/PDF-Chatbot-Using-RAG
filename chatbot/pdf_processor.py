from langchain_community.document_loaders import PyPDFLoader


class PDFProcessor:
    def __init__(self,filepath):
        filepath = filepath
    
    def load_pdf(self):
        """
        This function uses PyPDFLoader to load the PDF file.

        Args:
            filepath: Contains the path of the PDF file to be loaded
        
        Returns: 
            PyPDFLoader object

        Raises:
            Exception: Unable to load PDF.

        """
        try:
            pdf_loader = PyPDFLoader(self.filepath)
            docs = pdf_loader.load()
            if docs:
                print(f"Document loaded succesfully: Sample {docs[:1]}")    
                return docs
            else:
                raise Exception("PDF loaded but contains no content.")
            
        except Exception as e:
            raise Exception(f"Unable to load PDF: {e}")


