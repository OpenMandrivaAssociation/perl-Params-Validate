%define	upstream_name	 Params-Validate
%define	upstream_version 0.92

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Validate method/function call parameters
License:	GPL+ or Artistic
Group:		Development/Other
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Params/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Attribute::Handlers)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Test::More)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Params::Validate module provides a flexible system for validation
method/function call parameters.

The validation can be as simple as checking for the presence of required
parameters or as complex as validating object classes (via isa) or capabilities
(via can), checking parameter types, and using customized callbacks to ensure
data integrity.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -fr %{buildroot}
%makeinstall_std

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/*
%{perl_vendorarch}/auto/Params
