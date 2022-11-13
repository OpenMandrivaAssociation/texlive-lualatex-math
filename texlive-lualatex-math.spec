Name:		texlive-lualatex-math
Version:	61464
Release:	1
Summary:	Fixes for mathematics-related LuaLaTeX issues
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/lualatex-math
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-math.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualatex-math.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/lualatex/lualatex-math
%doc %{_texmfdistdir}/doc/lualatex/lualatex-math
#- source
%doc %{_texmfdistdir}/source/lualatex/lualatex-math

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
