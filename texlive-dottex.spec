# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/dottex
# catalog-date 2007-08-21 11:49:34 +0200
# catalog-license gpl
# catalog-version 0.6
Name:		texlive-dottex
Version:	0.6
Release:	5
Summary:	Use dot code in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dottex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6-2
+ Revision: 751067
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.6-1
+ Revision: 718251
- texlive-dottex
- texlive-dottex
- texlive-dottex
- texlive-dottex

