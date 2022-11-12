Name:		texlive-dottex
Version:	15878
Release:	1
Summary:	Use dot code in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dottex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The dottex package allows you to encapsulate 'dot' and 'neato'
files in your document (dot and neato are both part of
graphviz; dot creates directed graphs, neato undirected
graphs). If you have shell-escape enabled, the package will
arrange for your files to be processed at LaTeX time;
otherwise, the conversion must be done manually as an
intermediate process before a second LaTeX run.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dottex/dottex.sty
%doc %{_texmfdistdir}/doc/latex/dottex/README
%doc %{_texmfdistdir}/doc/latex/dottex/dottex.pdf
%doc %{_texmfdistdir}/doc/latex/dottex/example.tex
%doc %{_texmfdistdir}/doc/latex/dottex/gpl.txt
#- source
%doc %{_texmfdistdir}/source/latex/dottex/dottex.dtx
%doc %{_texmfdistdir}/source/latex/dottex/dottex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
