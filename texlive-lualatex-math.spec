# revision 24009
# category Package
# catalog-ctan /macros/luatex/latex/lualatex-math
# catalog-date 2011-09-18 21:09:14 +0200
# catalog-license lppl1.3
# catalog-version 0.3b
Name:		texlive-lualatex-math
Version:	0.3b
Release:	2
Summary:	Fixes for mathematics-related LuaLaTeX issues
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/lualatex-math
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-math.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-math.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-math.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package patches a few commands of the LaTeX2e kernel and
the amsmath and mathtools packages to be more compatible with
the LuaTeX engine. It is only meaningful for LuaLaTeX documents
containing mathematical formulas, and does not exhibit any new
functionality. The fixes are mostly moved from the unicode-math
package to this package since they are not directly related to
Unicode mathematics typesetting.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/lualatex/lualatex-math/lualatex-math.lua
%{_texmfdistdir}/tex/lualatex/lualatex-math/lualatex-math.sty
%doc %{_texmfdistdir}/doc/lualatex/lualatex-math/lualatex-math.pdf
#- source
%doc %{_texmfdistdir}/source/lualatex/lualatex-math/lualatex-math.dtx
%doc %{_texmfdistdir}/source/lualatex/lualatex-math/lualatex-math.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
