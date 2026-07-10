%global tl_name dottex
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Use dot code in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dottex
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dottex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The dottex package allows you to encapsulate 'dot' and 'neato' files in
your document (dot and neato are both part of graphviz; dot creates
directed graphs, neato undirected graphs). If you have shell-escape
enabled, the package will arrange for your files to be processed at
LaTeX time; otherwise, the conversion must be done manually as an
intermediate process before a second LaTeX run.

