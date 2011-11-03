# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cuisine
# catalog-date 2006-12-09 15:50:57 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-cuisine
Version:	0.5
Release:	1
Summary:	Typeset recipes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cuisine
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuisine.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuisine.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuisine.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Typeset recipes with the ingredients lined up with their method
step (somewhat similarly to the layout used in cooking).

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
%{_texmfdistdir}/tex/latex/cuisine/cuisine.sty
%doc %{_texmfdistdir}/doc/latex/cuisine/README
%doc %{_texmfdistdir}/doc/latex/cuisine/cuisine.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cuisine/cuisine.dtx
%doc %{_texmfdistdir}/source/latex/cuisine/cuisine.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
