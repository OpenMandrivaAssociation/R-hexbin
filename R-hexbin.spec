%global packname  hexbin
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.26.1
Release:          1
Summary:          Hexagonal Binning Routines
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/hexbin_1.26.1.tar.gz
Requires:         R-methods R-grid R-lattice R-graphics R-grDevices
Requires:         R-stats R-utils R-marray R-affy R-Biobase
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-grid R-lattice R-graphics R-grDevices
BuildRequires:    R-stats R-utils R-marray R-affy R-Biobase

%description
Binning and plotting functions for hexagonal bins. Now uses and relies on
grid graphics and formal (S4) classes and methods.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
