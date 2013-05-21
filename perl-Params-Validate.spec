%define	modname	Params-Validate
%define	modver	1.06

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	5
Summary:	Validate method/function call parameters
License:	GPL+ or Artistic
Group:		Development/Other
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Params/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Attribute::Handlers)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl-devel >= 2:5.14
BuildRequires:	perl-List-MoreUtils >= 0.320.0-3

%description
The Params::Validate module provides a flexible system for validation
method/function call parameters.

The validation can be as simple as checking for the presence of required
parameters or as complex as validating object classes (via isa) or capabilities
(via can), checking parameter types, and using customized callbacks to ensure
data integrity.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/*

%changelog
* Fri Dec 28 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.60.0-4
- rebuild for perl-5.16.2
- cleanups

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3
+ Revision: 765584
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.0.0-2
+ Revision: 763981
- Build for perl 5.14

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1
+ Revision: 684781
- update to new version 1.00

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.990.0-1
+ Revision: 682140
- update to new version 0.99

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.980.0-1
+ Revision: 662758
- new version

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.950.0-3mdv2011.0
+ Revision: 564573
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.950.0-2mdv2011.0
+ Revision: 555276
- rebuild

* Tue Feb 16 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.950.0-1mdv2010.1
+ Revision: 506750
- update to 0.95

* Fri Dec 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.940.0-1mdv2010.1
+ Revision: 473276
- fix format security
- update to 0.94

* Tue Dec 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.930.0-1mdv2010.1
+ Revision: 472245
- update to 0.93

* Sun Sep 27 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.0
+ Revision: 449779
- update to 0.92

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.910.0-1mdv2010.0
+ Revision: 404283
- rebuild using %%perl_convert_version

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 0.91-2mdv2009.1
+ Revision: 366061
- fix str fmt

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.91-2mdv2009.0
+ Revision: 265430
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-1mdv2009.0
+ Revision: 202292
- new version
- update to new version 0.91

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.89-2mdv2008.1
+ Revision: 151322
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.89-1mdv2008.1
+ Revision: 105306
- update to new version 0.89

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.88-2mdv2008.0
+ Revision: 90065
- rebuild

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.88-1mdv2008.0
+ Revision: 20318
- 0.88


* Wed Aug 09 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-09 17:46:48 (54825)
- Version 0.86

* Wed Aug 09 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-09 17:44:18 (54823)
- import perl-Params-Validate-0.85-1mdv2007.0

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.85-1mdv2007.0
- New version 0.85

* Mon May 29 2006 Scott Karns <scottk@mandriva.org> 0.84-1mdv2007.0
- 0.84

* Mon May 29 2006 Scott Karns <scottk@mandriva.org> 0.83-2mdv2007.0
- Added BuildRequires ExtUtils::CBuilder

* Sat May 27 2006 Scott Karns <scottk@mandriva.org> 0.83-1mdv2007.0
- 0.83

* Tue May 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.82-1mdk
- 0.82

* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.81-1mdk
- New release 0.81
- fix source URL

* Tue Jan 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.80-1mdk
- 0.80

* Fri Jan 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.79-1mdk
- new version
- spec cleanup
- %%{1}mdv2007.0
- rpmbuildupdate aware

* Wed Jul 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.78-1mdk
- 0.78

* Mon May 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.77-1mdk
- 0.77
- add tests ; spec cleanup

* Fri Nov 19 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.76-1mdk
- New release 0.76

* Tue May 11 2004 Michael Scherer <misc@mandrake.org> 0.74-1mdk
- New release 0.74

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 0.65-1mdk
- 0.65.

