from autocv.models.schemas import CVRequest


def generate_cv(data: CVRequest) -> str:
    """Create a CV document from input data.

    Placeholder implementation. Integrate a template engine (e.g., docxtpl)
    and PDF conversion tools to produce an ATS-friendly document.
    """
    # TODO: implement document generation
    return "generated_cv.docx"
