Name:		texlive-cuisine
Version:	34453
Release:	1
Summary:	Typeset recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cuisine
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuisine.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuisine.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuisine.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typeset recipes with the ingredients lined up with their method
step (somewhat similarly to the layout used in cooking).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cuisine/cuisine.sty
%doc %{_texmfdistdir}/doc/latex/cuisine/README
%doc %{_texmfdistdir}/doc/latex/cuisine/cuisine.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cuisine/cuisine.dtx
%doc %{_texmfdistdir}/source/latex/cuisine/cuisine.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
