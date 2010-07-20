%define	upstream_name	 Params-Validate
%define upstream_version 0.95

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Validate method/function call parameters
License:	GPL+ or Artistic
Group:		Development/Other
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Params/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:     Params-Validate-0.94-format-security.patch

BuildRequires:	perl(Attribute::Handlers)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

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
%patch0 -b .fmtsec

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -fr %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/*
%{perl_vendorarch}/auto/Params
