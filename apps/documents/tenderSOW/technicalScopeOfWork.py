import os
import sys
import subprocess
from pylatex import (
            Document,
            Package, 
            PageStyle, 
            Head, 
            Section,
            Itemize,
            Tabular, 
            Center, 
            Subsection, 
            Subsubsection,
            Foot, 
            simple_page_number, 
            Command, 
            MiniPage, 
            Figure,
            SubFigure,
            StandAloneGraphic, 
            LargeText, 
            MediumText, 
            VerticalSpace, 
            Tabu, 
            FlushLeft, 
            Math,
            NoEscape,
     
)
from pylatex.basic import NewLine, NewPage, LineBreak, Environment
from pylatex.base_classes.command import Options
from pylatex.lists import List
from pylatex.utils import rm_temp_dir, bold, italic, fix_filename
from pylatexenc import latexencode
from calculations import *
from worksorderdata import *
import sympy as sp
from sympy import *


def main():
    margins = {
        'tmargin': '20mm',
        'bmargin': '20mm',
        'lmargin': '20mm',
        'rmargin': '20mm'
    }

    doc = Document(documentclass='article', document_options=None, lmodern=None, fontenc = ['T2A', 'T1'], textcomp=None, page_numbers=None, indent=True, data=None, geometry_options=margins)
    doc.packages.add(Package('newtxtext, newtxmath'))
    doc.packages.add(Package('substitutefont'))
    doc.packages.add(Package('lastpage'))
    doc.packages.add(Package('gensymb'))

    doc.preamble.append(Command(r'linespread', arguments='1.5'))
    doc.preamble.append(Command('usepackage', 'newunicodechar'))


    # ALL PAGES ======================================================================#
    # Extracted from workorderdat.py
    head_of_page = PageStyle('header', header_thickness=0.5, footer_thickness=1.0)
    with head_of_page.create(Head("C")):
        head_of_page.append(DOC_TITLE)
        doc.preamble.append(head_of_page)
        doc.change_document_style('header')

    with head_of_page.create(Foot("L")) as foot1:
        foot1.append(FILENAME)

    with head_of_page.create(Foot("R")) as foot2:
        num_of_pages = simple_page_number()
        foot2.append(num_of_pages)

    # COVER PAGE ====================================================================#
    # Extracted from workorderdat.py
    with doc.create(Center()) as center:
        with center.create(Section("")) as sec:
            sec.numbering = None
            with sec.create(MiniPage(align='c')) as title:
                
                title.append(LargeText(bold(DESIGN_COMPANY)))
                title.append(VerticalSpace('20pt'))
                title.append(LineBreak())
                title.append(MediumText(bold(PROJECT_NAME)))
                title.append(VerticalSpace('20pt'))
                title.append(LineBreak())
                title.append(MediumText(bold(PROJECT_NUMBER)))
                title.append(VerticalSpace('20pt'))
                title.append(LineBreak())
                title.append(MediumText(bold(FILENAME)))
                title.append(VerticalSpace('80pt'))

    with doc.create(Center()) as pos:
        with pos.create(MiniPage(align='l')) as tab:
            with tab.create(Tabular('|l |l |')) as table:
                table.add_hline()
                table.add_row((bold("Engineer:"), ENGINEER))
                table.add_hline(1, 2)
                table.add_row((bold("Registration:"), ECSA))
                table.add_hline(1, 2)
                table.add_row((bold("Email:"), COMPANY_EMAIL))
                table.add_hline(1, 2)
                table.add_row((bold("Phone:"), PHONE))
                table.add_hline(1, 2)
                table.add_row((bold("Adress:"), ADDRESS_1))
                table.add_hline(1, 2)
                table.add_row((bold(""), ADDRESS_2))
                table.add_hline(1, 2)
                table.add_row((bold(""), ADDRESS_3))
                table.add_hline(1, 2)
                table.add_row((bold("Website:"), WEBSITE))
                table.add_hline(1, 2)
            pos.append(VerticalSpace('150pt'))
            pos.append(Command('centering'))

    with doc.create(Figure(position='h!')) as fig:
        fig.append(StandAloneGraphic(
                image_options="width=240px",
                filename=fix_filename(LOGO)
                ))
        fig.append(Command('centering'))

    doc.append(NewPage())

    # SECTION 1 ======================================================================#
    # Extracted from workorderdat.py
    with doc.create(Center()) as center:
        with center.create(Section(SECTION_1)) as sec:
            sec.numbering = None


        with center.create(MiniPage(align='c')) as tab:
            with tab.create(Tabular('|c |c |c |c |c |c |')) as table:
                table.add_hline()
                table.add_row((
                                bold("REV"), 
                                bold("DESCRIPTION"), 
                                bold("DATE"), 
                                bold("ISSUED BY"), 
                                bold("REVIEWED BY"), 
                                bold("APPROVED")
                                ))
                table.add_hline()

    # doc.append(REVISION_TABLE)
    doc.append(NewPage())

    # SECTION 2 ======================================================================#
    with doc.create(Section(SECTION_2)):
        with doc.create(FlushLeft()) as left:
            with left.create(MiniPage(align='c')) as tab:
                with tab.create(Tabular('|l |l |')) as table:
                    table.add_hline()
                    table.add_row((bold("Customer:"), CUSTOMER_COMPANY))
                    table.add_hline(1, 2)
                    table.add_row((bold("Customer Name:"), CUSTOMER))
                    table.add_hline(1, 2)
                    table.add_row((bold("Customer Email:"), EMAIL))
                    table.add_hline(1, 2)
            
    doc.append(NewPage())

    # SECTION 3: DRAWING AND SKETCHES=====================================================================#
    with doc.create(Section(SECTION_3)) as sec:
        # General project data	
        with sec.create(Subsection(SECTION_3_1)) as subsec1:
            list_data = designCodes()
            with subsec1.create(FlushLeft()):
                for item in list_data:
                    subsec1.append(item)
                    subsec1.append(LineBreak())
        # General site conditions				
        with sec.create(Subsection(SECTION_3_2)) as subsec2:
            list_data = general_data()
            with subsec2.create(FlushLeft()) as left:
                with left.create(MiniPage(align='l')) as tab:
                    with tab.create(Tabular('|l |l |c|')) as table:
                        for k,v in list_data.items():
                            if v[2] != "":
                                unit = (Math(inline = True, data = [v[2]], escape = False))
                            else:
                                unit = ""
                            table.add_hline()
                            table.add_row((bold(v[0]), str(v[1]), unit))
                        table.add_hline()    
            list_data =[]
        doc.append(NewPage())

        # General sketches and drawings
        with sec.create(Subsection(SECTION_3_3)) as subsec4:
            with subsec4.create(Subsubsection("Basic Flow Diagram")) as subsubsec4:
                with subsubsec4.create(Figure(position='h!')) as fig:
                    fig.append(StandAloneGraphic(
                            image_options= SKETCH_1[1],
                            filename=fix_filename(SKETCH_1[0])
                            ))
                    fig.append(Command('centering'))
                    fig.add_caption(SKETCH_1[2])
                    fig.append(Command('centering'))
                    

            with subsec4.create(Subsubsection("General Layout")) as subsubsec5:
                with subsubsec5.create(Figure(position='h!')) as fig:
                    with fig.create(SubFigure(
                            position='b',
                            width=NoEscape(r'0.45\linewidth'))) as left_fig:

                        left_fig.add_image(SKETCH_2[0],
                                            width=SKETCH_2[1])
                        left_fig.append(Command('centering'))                    
                        left_fig.add_caption(SKETCH_2[2])

                subsubsec5.append(NewPage())

            with subsec4.create(Subsubsection("River Abstraction Detail")) as subsubsec6:
                with subsubsec6.create(Figure(position='h!')) as fig:
                    with fig.create(SubFigure(
                            position='b',
                            width=NoEscape(r'0.45\linewidth'))) as left_fig:

                        left_fig.add_image(SKETCH_3[0],
                                            width=SKETCH_3[1])
                        left_fig.append(Command('centering'))                    
                        left_fig.add_caption(SKETCH_3[2])

            
                with subsubsec6.create(Figure(position='h!')) as fig:
                    with fig.create(SubFigure(
                            position='b',
                            width=NoEscape(r'0.45\linewidth'))) as left_fig:

                        left_fig.add_image(SKETCH_4[0],
                                            width=SKETCH_4[1])
                        left_fig.append(Command('centering'))                    
                        left_fig.add_caption(SKETCH_4[2])

        
                with subsubsec6.create(Figure(position='h!')) as fig:
                    with fig.create(SubFigure(
                            position='b',
                            width=NoEscape(r'0.45\linewidth'))) as left_fig:

                        left_fig.add_image(SKETCH_5[0],
                                            width=SKETCH_5[1])
                        left_fig.append(Command('centering'))                    
                        left_fig.add_caption(SKETCH_5[2])

           
                with subsubsec6.create(Figure(position='h!')) as fig:
                    with fig.create(SubFigure(
                            position='b',
                            width=NoEscape(r'0.45\linewidth'))) as left_fig:

                        left_fig.add_image(SKETCH_6[0],
                                            width=SKETCH_6[1])
                        left_fig.append(Command('centering'))                    
                        left_fig.add_caption(SKETCH_6[2])
                

    doc.append(NewPage())
    # SECTION 4: BACKGROUND ======================================================================#
    with doc.create(Section(SECTION_4)) as sec:                
        with sec.create(Subsection(SECTION_4_1)) as subsec2:
            subsec2.append(NoEscape(TEXT1))
            subsec2.append('\n')
            subsec2.append('\n')
            subsec2.append(NoEscape(TEXT2))

        with sec.create(Subsection(SECTION_4_2)) as subsec3:
            subsec3.append(NoEscape(TEXT3))
            subsec3.append('\n')
            subsec3.append('\n')
            subsec3.append(NoEscape(TEXT4))
            with subsec3.create(Itemize()) as itemize:
                itemize.add_item(BULLET1)
                itemize.add_item(BULLET2)
                itemize.add_item(BULLET3)
                itemize.add_item(BULLET4)
                itemize.add_item(BULLET5)
                itemize.add_item(BULLET6)
                itemize.append(Command("ldots"))

        with sec.create(Subsection(SECTION_4_3)) as subsec4:
            subsec4.append(NoEscape(TEXT5))
            subsec4.append('\n')
            subsec4.append('\n')
            subsec4.append(NoEscape(TEXT6))
            with subsec4.create(Itemize()) as itemize:
                itemize.add_item(BULLET7)
                itemize.add_item(BULLET8)
                itemize.add_item(BULLET9)
                # you can append to existing items
                itemize.append(Command("ldots"))

        

        
    doc.append(NewPage())  
    # SECTION 5: SCOPE OF WORK ======================================================================#
    # with doc.create(Section(SECTION_5)) as sec:
    #     with sec.create(Subsection(SECTION_5_1)) as subsec2:
    #         with subsec2.create(FlushLeft()) as left:
    #             with left.create(MiniPage(align='l')) as tab:
    #                     pass

    #     with sec.create(Subsection(SECTION_5_2)) as subsec3:
    #         with subsec2.create(FlushLeft()) as left:
    #             with left.create(MiniPage(align='l')) as tab:
    #                     pass

    #     with sec.create(Subsection(SECTION_5_3)) as subsec4:
    #         with subsec3.create(FlushLeft()) as left:
    #             with left.create(MiniPage(align='l')) as tab:
    #                     pass

    #     with sec.create(Subsection(SECTION_5_4)) as subsec5:
    #         with subsec5.create(FlushLeft()) as left:
    #             with left.create(MiniPage(align='l')) as tab:
    #                     pass
        
    #     sec.append(NewPage()) 
       
    cwd = os.getcwd()
    print(cwd)
    cwd = cwd+'\\apps'+'\\documents'+'\\tenderSOW\\'
    doc.generate_tex(cwd+FILENAME)
    # doc.generate_pdf(cwd+FILENAME, clean_tex=False, compiler='latexmk', compiler_args=['-c'])
    path = cwd+FILENAME+'.tex'
    subprocess.Popen([path], shell=True)

if __name__ == main():
    main()