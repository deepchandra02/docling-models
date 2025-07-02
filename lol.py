from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import EasyOcrOptions, PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

artifacts_path = r"lib/docling-model-artifacts"

pipeline_options = PdfPipelineOptions(artifacts_path=artifacts_path)
doc_converter = DocumentConverter(
    format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
)

source = r"transfer-to-pension-fund-or-vested-benefits-foundation-en.pdf"

doc = doc_converter.convert(source).document
print(doc.export_to_markdown())
