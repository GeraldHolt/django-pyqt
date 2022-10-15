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
            Enumerate,
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
                list_data = REVISIONS
                for k, v in list_data.items():
                            table.add_row(v[0], v[1], v[2], v[3], v[4], v[5])
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
            with subsec1.create(FlushLeft()) as left:
                with left.create(MiniPage(align='l')) as tab:
                    with tab.create(Tabular('|l |l |')) as table:
                        for v in list_data:
                            table.add_hline()
                            table.add_row((bold(v[0]), str(v[1])))
                        table.add_hline()    
            list_data =[]
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

        with sec.create(Subsection(SECTION_4_3)) as subsec4:
            subsec4.append(NoEscape(TEXT5))
            subsec4.append('\n')
            subsec4.append('\n')
            subsec4.append(NoEscape(TEXT6))
            with subsec4.create(Itemize()) as itemize:
                itemize.add_item(BULLET7)
                itemize.add_item(BULLET8)
                itemize.add_item(BULLET9)

    doc.append(NewPage())  
    #SECTION 5: SCOPE OF WORK ======================================================================#
    with doc.create(Section(SECTION_5)) as sec:
        with sec.create(Subsection(SECTION_5_1)) as subsec2:
            subsec2.append(NoEscape(TEXT7))
            subsec2.append('\n')
            subsec2.append('\n')
            subsec2.append(NoEscape(TEXT8))
            with subsec2.create(Itemize()) as itemize:
                itemize.add_item(BULLET10)
                itemize.add_item(BULLET11)
                itemize.add_item(BULLET12)
                
        with sec.create(Subsection(SECTION_5_2)) as subsec3:
            with subsec3.create(Subsubsection(SECTION_5_2_1)) as subsubsec3:
                with subsubsec3.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT1)
                    enum.add_item(POINT2)
                    enum.add_item(POINT3)
                    enum.add_item(POINT4)
                    enum.add_item(POINT5)
                    enum.add_item(POINT6)
                    enum.add_item(POINT7)
                    enum.add_item(POINT8)
                    enum.add_item(POINT9)
                    enum.add_item(POINT10)
                    enum.add_item(POINT11)
                    enum.add_item(POINT12)
                    enum.add_item(POINT13)
                    enum.add_item(POINT14)
                    enum.add_item(POINT15)
                    enum.add_item(POINT16)
                    enum.add_item(POINT17)
                    enum.add_item(POINT18)
                    enum.add_item(POINT19)
                    enum.add_item(POINT20)
                    enum.add_item(POINT21)
        
            with subsec3.create(Subsubsection(SECTION_5_2_2)) as subsubsec4:
                with subsubsec4.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT22)
                    enum.add_item(POINT23)
        with sec.create(Subsection(SECTION_5_3)) as subsec4:
            with subsec4.create(Subsubsection(SECTION_5_3_1)) as subsubsec5:
                with subsubsec5.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT24)
            with subsec4.create(Subsubsection(SECTION_5_3_2)) as subsubsec6:
                with subsubsec6.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT25)
            with subsec4.create(Subsubsection(SECTION_5_3_2)) as subsubsec7:
                with subsubsec7.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT26)
            with subsec4.create(Subsubsection(SECTION_5_3_2)) as subsubsec8:
                with subsubsec8.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT27)
            with subsec4.create(Subsubsection(SECTION_5_3_2)) as subsubsec9:
                with subsubsec8.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT28)
        
        with sec.create(Subsection(SECTION_5_4)) as subsec5:
            with subsec5.create(Subsubsection(SECTION_5_4_1)) as subsubsec10:
                with subsubsec10.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT29)
                    enum.add_item(POINT30)

            with subsec5.create(Subsubsection(SECTION_5_4_1)) as subsubsec11:
                with subsubsec11.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT31)

            with subsec5.create(Subsubsection(SECTION_5_4_1)) as subsubsec12:
                with subsubsec12.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT32)

        with sec.create(Subsection(SECTION_5_5)) as subsec6:
            with subsec6.create(Subsubsection(SECTION_5_5_1)) as subsubsec13:
                with subsubsec13.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT33)
                
            with subsec6.create(Subsubsection(SECTION_5_5_2)) as subsubsec14:
                with subsubsec14.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT34)

            with subsec6.create(Subsubsection(SECTION_5_5_3)) as subsubsec15:
                with subsubsec15.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT35)

            with subsec6.create(Subsubsection(SECTION_5_5_4)) as subsubsec16:
                with subsubsec16.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT36)

        with sec.create(Subsection(SECTION_5_6)) as subsec6:
            with subsec6.create(Subsubsection(SECTION_5_6_1)) as subsubsec17:
                with subsubsec17.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT37)

            with subsec6.create(Subsubsection(SECTION_5_6_2)) as subsubsec18:
                with subsubsec18.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT38)

            with subsec6.create(Subsubsection(SECTION_5_6_3)) as subsubsec19:
                with subsubsec19.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT39)

            with subsec6.create(Subsubsection(SECTION_5_6_4)) as subsubsec19:
                with subsubsec19.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT40)

            with subsec6.create(Subsubsection(SECTION_5_6_5)) as subsubsec20:
                with subsubsec20.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT40a)
                    enum.add_item(POINT41)
                    enum.add_item(POINT42)
                    
            with subsec6.create(Subsubsection(SECTION_5_6_6)) as subsubsec21:
                with subsubsec21.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT43)
                    enum.add_item(POINT44)
                    enum.add_item(POINT45)
                    enum.add_item(POINT46)
                    enum.add_item(POINT47)
                    enum.add_item(POINT48)
                    enum.add_item(POINT49)

            with subsec6.create(Subsubsection(SECTION_5_6_7)) as subsubsec22:
                with subsubsec22.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT50)
                    enum.add_item(POINT51)
                    enum.add_item(POINT52)
                    enum.add_item(POINT53)

            with subsec6.create(Subsubsection(SECTION_5_6_8)) as subsubsec23:
                with subsubsec23.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT54)
                    enum.add_item(POINT55)
                    enum.add_item(POINT56)
                    enum.add_item(POINT57)
                    enum.add_item(POINT58)
                    enum.add_item(POINT59)
                    enum.add_item(POINT60)
                    enum.add_item(POINT61)
                    enum.add_item(POINT62)

            with subsec6.create(Subsubsection(SECTION_5_6_9)) as subsubsec24:
                with subsubsec24.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT62a)
                    enum.add_item(POINT63)
                    enum.add_item(POINT64)

            with subsec6.create(Subsubsection(SECTION_5_6_10)) as subsubsec25:
                with subsubsec25.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT65)
                    enum.add_item(POINT66)
                    enum.add_item(POINT67)
                    enum.add_item(POINT68)
                    enum.add_item(POINT69)
                    enum.add_item(POINT70)
                    enum.add_item(POINT71)
                    enum.add_item(POINT72)
                    with enum.create(Itemize()) as itemize:
                        itemize.add_item(BUL1)
                        itemize.add_item(BUL2)
                        itemize.add_item(BUL3)
                        itemize.add_item(BUL4)
                    enum.add_item(POINT73)

        with sec.create(Subsection(SECTION_5_7)) as subsec7:
            with subsec7.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT74)

        with sec.create(Subsection(SECTION_5_8)) as subsec8:
            with subsec8.create(Subsubsection(SECTION_5_8_1)) as subsubsec26:
                with subsubsec26.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT75)
                    enum.add_item(POINT76)

            with subsec8.create(Subsubsection(SECTION_5_8_2)) as subsubsec27:
                with subsubsec27.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT77)
                    enum.add_item(POINT78)
                    enum.add_item(POINT79)

            with subsec8.create(Subsubsection(SECTION_5_8_3)) as subsubsec28:
                with subsubsec28.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT80)
                    with enum.create(Itemize()) as itemize:
                        itemize.add_item(BUL5)
                        itemize.add_item(BUL6)

        with sec.create(Subsection(SECTION_5_9)) as subsec9:
            with subsec9.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT81)
                    enum.add_item(POINT82)
                    enum.add_item(POINT83)

        with sec.create(Subsection(SECTION_5_10)) as subsec10:
            with subsec10.create(Enumerate(enumeration_symbol=r"\alph*)", options={'start': 1})) as enum:
                    enum.add_item(POINT84)
                    with enum.create(Itemize()) as itemize:
                        itemize.add_item(BUL7)
                        itemize.add_item(BUL8)
                        itemize.add_item(BUL9)
                    enum.add_item(POINT85)
                    enum.add_item(POINT86)
                    enum.add_item(POINT87)
                    with enum.create(Itemize()) as itemize:
                        itemize.add_item(BUL10)
                        itemize.add_item(BUL11)
                        itemize.add_item(BUL12)
                        itemize.add_item(BUL13)
                    enum.add_item(POINT88)
                    with enum.create(Itemize()) as itemize:
                        itemize.add_item(BUL14)
                        itemize.add_item(BUL15)
                        itemize.add_item(BUL16)
                        itemize.add_item(BUL17)
                        itemize.add_item(BUL18)

    #SECTION 6: BILL OF QUANTITIES ======================================================================#
    with doc.create(Section(SECTION_6)) as sec:
        with sec.create(Subsection(SECTION_6_1)) as subsec2:
            subsec2.append('Refer to the drawing register for the latest revision')
            list_data = applicableDrawings()
            with subsec2.create(FlushLeft()) as left:
                with left.create(MiniPage(align='l')) as tab:
                    with tab.create(Tabular('|l |l |')) as table:
                        for k,v in list_data.items():
                            table.add_hline()
                            table.add_row((v[0]), bold(str(v[1])))
                        table.add_hline()    
            list_data =[]

        with sec.create(Subsection(SECTION_6_2)) as subsec3:
            subsec3.append("Refer to the detailed bill of quantities schedule.")

    #SECTION 7: METHODOLOGY ======================================================================#
    with doc.create(Section(SECTION_7)) as sec:
        with sec.create(Subsection(SECTION_7_1)) as subsec2:
            subsec2.append(NoEscape(TEXT7_1))
            subsec2.append('\n')
            subsec2.append('\n') 
            subsec2.append(NoEscape(TEXT7_2))
            subsec2.append('\n')
            subsec2.append('\n') 
            subsec2.append(NoEscape(TEXT7_3))   
            subsec2.append('\n')
            subsec2.append('\n') 
            subsec2.append(NoEscape(TEXT7_4))   
            subsec2.append('\n')
            subsec2.append('\n') 
            subsec2.append(NoEscape(TEXT7_5))   
            subsec2.append('\n')
            subsec2.append('\n') 
            subsec2.append(NoEscape(TEXT7_6))  

        with sec.create(Subsection(SECTION_7_2)) as subsec3:
            subsec3.append(NoEscape(TEXT_7_6))
            subsec3.append('\n')
            subsec3.append('\n') 
            subsec3.append(NoEscape(TEXT_7_7))
            subsec3.append('\n')
            subsec3.append('\n') 
            subsec3.append(NoEscape(TEXT_7_8))

        sec.append(NewPage()) 
       
    cwd = os.getcwd()
    print(cwd)
    cwd = cwd+'\\apps'+'\\documents'+'\\tenderSOW\\'
    doc.generate_tex(cwd+FILENAME)
    # doc.generate_pdf(cwd+FILENAME, clean_tex=False, compiler='latexmk', compiler_args=['-c'])
    path = cwd+FILENAME+'.tex'
    subprocess.Popen([path], shell=True)

if __name__ == main():
    main()