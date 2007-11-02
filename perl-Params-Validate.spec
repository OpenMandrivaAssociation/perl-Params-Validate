%define	module	Params-Validate
%define	name	perl-%{module}
%define	version	0.89
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Validate method/function call parameters
License:	GPL or Artistic
Group:		Development/Other
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/Params/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Attribute::Handlers)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Test::More)
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Params::Validate module provides a flexible system for validation
method/function call parameters.

The validation can be as simple as checking for the presence of required
parameters or as complex as validating object classes (via isa) or capabilities
(via can), checking parameter types, and using customized callbacks to ensure
data integrity.

%prep

%setup -q -n %{module}-%{version}

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
%{perl_vendorarch}/Params
%{perl_vendorarch}/Attribute
%{perl_vendorarch}/auto/Params



