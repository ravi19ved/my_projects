%*************************************
% UQ Thesis Formatting Style Class
%*************************************
% uqthesis.cls

% This file defines the formatting style for your thesis in accordance with the Thesis Format Requirements.
% Your thesis needs to comply with the formatting requirements outlined in the Higher Degree by Research Thesis Examination Procedures:
% - Procedures with Oral Examination: https://policies.uq.edu.au/document/view-current.php?id=248
% - Procedures without Oral Examination: https://policies.uq.edu.au/document/view-current.php?id=249
% The most appropriate referencing style will depend on your discipline and your advisory team will be able to provide advice on disciplinary norms.

%*************************************
% Class structure: identification part
%*************************************

\ProvidesClass{StylesAndSettings/uqthesis}[2025/05/23 version 2.01 UQ PhD and Masters thesis style]
\NeedsTeXFormat{LaTeX2e}[2023-11-01]

% Load the memoir class.
\LoadClass[12pt, a4paper, openany]{memoir}
% LaTeX forces chapters to start on right-hand (odd) pages by inserting a blank right-hand (even) page if needed. openany turns this feature off. 

%*************************************
% Load packages
%*************************************
\RequirePackage{mathptmx} 							
%Set the font to Times New Roman. This package also alters the math-mode font to TNR.

\RequirePackage{graphicx}								
% Use pdfLaTeX.

\RequirePackage{booktabs, longtable} 		
% These allow tables to split over pages. Very useful in theses!

\RequirePackage{url} 									
% Typeset urls properly.

\RequirePackage{hyperref}							
% Hyperlink your pdf output.

\RequirePackage{geometry}								
% This allows us to set the margins correctly.

\RequirePackage{memhfixc}							
% Need this to make sure the layout is correct.
	
\RequirePackage{amsmath,amssymb,amsthm} 
% Useful maths packages.

\RequirePackage{setspace}								
%Used to set the appropriate linespacing.

\RequirePackage{StylesAndSettings/uqtitle}								
%Get the title page right.

\RequirePackage{comment}								
%Use this to enable easy inclusion/exclusion of instructions (at request of grad school).

\RequirePackage{enumitem}
%Used to get appropriate list spacing

\RequirePackage{xcolor}
%Used to get UQ Purple in the instructional notes

%*************************************
% Turn off instructional comments
%*************************************
%This section of code allows the template user to turn off the instructional comments with a single option.
%Adapted from https://tex.stackexchange.com/questions/135248/if-not-declareoption
	\newif\ifmycomments@comments
	\DeclareOption{instructions}{\mycomments@commentstrue}
	\DeclareOption{final}{\mycomments@commentsfalse}

	\ExecuteOptions{draft} % default is to have no comments.
	\excludecomment{instructional}

	\ProcessOptions\relax

	\ifmycomments@comments
		\includecomment{instructional} %include comments if true
        % Colour the instructions Purple
        % (not using #51247A, as too hard to distinguish from black)
        \definecolor{UQPurple}{HTML}{7030A0}

        \specialcomment{instructional}{%
        \begingroup\color{UQPurple}}{%
         \endgroup}
	\fi

%*************************************
% Set page and heading styles
%*************************************
% ********* Set page layout **********
\setlrmarginsandblock{20mm}{20mm}{*}
\setulmarginsandblock{20mm}{20mm}{*}

\setheadfoot{15mm}{\baselineskip}
\setheaderspaces{*}{\baselineskip}{*}

\def\baselinestretch{1.1}

%Make sure that TeX sorts out the geometry correctly.
\checkandfixthelayout

% ********* Chapter and section style **********
\makechapterstyle{mychapterstyle}{%
    \setlength{\beforechapskip}{0pt}%
    \renewcommand{\chapnamefont}{\Huge\rmfamily\bfseries}%
    \renewcommand{\chapnumfont}{\Huge\rmfamily\bfseries}%
    \renewcommand{\chaptitlefont}{\Huge\rmfamily\bfseries}%
    \renewcommand{\printchaptername}{\chapnamefont\chapnamefont Chapter}%
    \renewcommand{\printchapternum}{\chapnumfont\thechapter}%
    \renewcommand{\afterchapternum}{: }% Adds colon and space after the number
}

\chapterstyle{mychapterstyle}

\setsecheadstyle{\LARGE\rmfamily\bfseries}
\setsubsecheadstyle{\Large\rmfamily\bfseries}
\setsubsubsecheadstyle{\large\rmfamily\bfseries}
\setparaheadstyle{\normalfont\rmfamily}


% ********* Table of contents style **********
\settocdepth{subsection}

\setsecnumdepth{subsection}
\maxsecnumdepth{subsection}
\settocdepth{subsection}
\maxtocdepth{subsection}

\renewcommand{\listfigurename}{List of Figures}
\renewcommand{\listtablename}{List of Tables}

\settowidth{\cftchapternumwidth}{Chapter 88: }
\renewcommand*{\cftchapterpresnum}{Chapter~}
\renewcommand*{\cftchapteraftersnum}{:~}

% Show dots between chapter and number (with same spacing as for subsections)
\renewcommand*{\cftchapterleader}{\cftdotfill{4}}

% ********* Figure and Table Caption style **********

\usepackage[format=plain,
            labelfont=it,
            textfont=it]{caption}

% ********* General page styles **********

%Get the correct line spacing. Note that \onehalfspacing DOES NOT work because of the way which LaTeX measures linespacing (which is different to Word).
\linespread{1.4}
%Make sure footnotes don't split over a page.
\interfootnotelinepenalty=10000

% Set the spacing between items in a list, and remove the indent
\setitemize{noitemsep, topsep=-1pt, leftmargin=*}

% Set the spacing between items in a list, and remove the indent
\setlist[enumerate]{noitemsep, topsep=-1pt, leftmargin=*}



%*************************************
% Fix white space to improve readability
%*************************************
%Redefine the sqrt command so that it puts a space after the surd.
%This makes AMSMATH much easier to read.
%COMMENT THIS OUT OR DELETE IF YOU DON'T WISH TO USE IT.
\let\SQRT\sqrt
\renewcommand{\sqrt}[1]{\ensuremath{\SQRT{#1} \;}}

% ********* Bibliography / References **********
\renewcommand\bibname{References} % Name the Bibliography as References
