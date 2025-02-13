Name:		texlive-lecturer
Version:	23916
Release:	2
Summary:	On-screen presentations for (almost) all formats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/lecturer
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lecturer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lecturer.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package creates slides for on-screen presentations based on
PDF features without manipulating TeX's typesetting process.
The presentation flow relies on PDF's abilities to display
content step by step. Features include: - Free positioning of
anything anywhere in painted areas on the slide, as well as in
the main textblock; - Numerous attributes to control the layout
and the presentation flow, from TeX's primitive dimensions to
the visibility of steps; - Feature inheritance from global to
local settings, with intermediate types; - Basic drawing
facilities to produce symbols, e.g., for list items or buttons;
- Colors, transparency, shades, and pictures; - Navigation with
links, pop-up menus, and customizable bookmarks; - Easy switch
between presentation and handout; and - PDF transitions.
Besides the traditional documentation, the distribution
includes visual documentation and six demo presentations
ranging from geometric abstraction to classic style to silly
video game. Lecturer is designed to work with all formats, but
presently fails with ConTeXt MkIV (because of clashes in
management of PDF objects, probably), works only with pdfTeX
and LuaTeX for the time being, and requires texapi and yax,
both v.1.02.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/lecturer/lecturer.sty
%{_texmfdistdir}/tex/generic/lecturer/lecturer.tex
%{_texmfdistdir}/tex/generic/lecturer/ltr-areas.tex
%{_texmfdistdir}/tex/generic/lecturer/ltr-graphics.tex
%{_texmfdistdir}/tex/generic/lecturer/ltr-job.tex
%{_texmfdistdir}/tex/generic/lecturer/ltr-navigation.tex
%{_texmfdistdir}/tex/generic/lecturer/ltr-slides.tex
%{_texmfdistdir}/tex/generic/lecturer/ltr-steps.tex
%{_texmfdistdir}/tex/generic/lecturer/t-lecturer.tex
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-BeamerCambridgeUS.pdf
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-BeamerCambridgeUS.tex
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-KitschScienceFiction.pdf
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-KitschScienceFiction.tex
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-Mondrian.pdf
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-Mondrian.tex
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-SimplePresentation.pdf
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-SimplePresentation.tex
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-SquaresOfAs.pdf
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-SquaresOfAs.tex
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-ThePoodleLectures.pdf
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-ThePoodleLectures.tex
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-VisualDoc.pdf
%doc %{_texmfdistdir}/doc/generic/lecturer/LecturerDemo-VisualDoc.tex
%doc %{_texmfdistdir}/doc/generic/lecturer/README
%doc %{_texmfdistdir}/doc/generic/lecturer/lecturer-doc.pdf
%doc %{_texmfdistdir}/doc/generic/lecturer/lecturer-doc.tex
%doc %{_texmfdistdir}/doc/generic/lecturer/universe.jpg

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
