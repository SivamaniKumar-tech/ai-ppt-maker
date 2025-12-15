from copy import deepcopy

def clone_slide(prs, slide):
    """
    Clone an existing slide including all shapes and styling.
    """
    blank_layout = prs.slide_layouts[6]  # Blank slide
    new_slide = prs.slides.add_slide(blank_layout)

    for shape in slide.shapes:
        new_element = deepcopy(shape.element)
        new_slide.shapes._spTree.insert_element_before(
            new_element, 'p:extLst'
        )

    return new_slide
