# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cuisine
# catalog-date 2006-12-09 15:50:57 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-cuisine
Version:	0.5
Release:	8
Summary:	Typeset recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cuisine
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuisine.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuisine.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuisine.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5-2
+ Revision: 750727
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5-1
+ Revision: 718184
- texlive-cuisine
- texlive-cuisine
- texlive-cuisine
- texlive-cuisine

