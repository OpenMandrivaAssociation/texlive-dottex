Name:		texlive-dottex
Version:	0.6
Release:	1
Summary:	Use dot code in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dottex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The dottex package allows you to encapsulate 'dot' and 'neato'
files in your document (dot and neato are both part of
graphviz; dot creates directed graphs, neato undirected
graphs). If you have shell-escape enabled, the package will
arrange for your files to be processed at LaTeX time;
otherwise, the conversion must be done manually as an
intermediate process before a second LaTeX run.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
