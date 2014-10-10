%define module	Device-Cdio

Name:		perl-%{module}
Version:	0.3.0
Release:	2
Summary:	Module for CD Input and Control library
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Device/%{module}-v%{version}.tar.gz
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl-version
BuildRequires:	libcdio-devel 
BuildRequires:	swig

%description
A module to make easier temporary directories deletion

%prep
%setup -q -n %{module}-v%{version}
chmod u+w -R .

%build
perl Build.PL installdirs=vendor
# M::B copy files read-only, forcing to use 
# a two-pass build command
# https://rt.cpan.org/Ticket/Display.html?id=42777
./Build CFLAGS="%{optflags}" || :
chmod u+w -R .
./Build CFLAGS="%{optflags}"

%check
# test suite doesn't pass
# http://rt.cpan.org/Public/Bug/Display.html?id=42779
#./Build test

%install
./Build install destdir=%{buildroot}

%files
%{perl_vendorarch}/*
%{_mandir}/*/*


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.0-1
+ Revision: 773532
- cleanup spec
- new version
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Götz Waschk <waschk@mandriva.org>
    - rebuild for new libcdio

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.2.4-11
+ Revision: 681406
- mass rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.2.4-10mdv2010.0
+ Revision: 440548
- rebuild

* Thu Feb 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.4-9mdv2009.1
+ Revision: 337930
- sync patches set with debian
- disable test suite, it doesn't work (http://rt.cpan.org/Public/Bug/Display.html?id=42779)

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.2.4-8mdv2009.0
+ Revision: 256674
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.2.4-6mdv2008.1
+ Revision: 151427
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 25 2007 Olivier Thauvin <nanardon@mandriva.org> 0.2.4-5mdv2008.1
+ Revision: 101935
- add forgotten files by mdvsys
- kill pod test, don't work
- stealing some debian patchs (fix build)
- workaround perm issue (ugly method, I agree)


* Thu Sep 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-07 01:49:10 (60449)
- Fix buildrequires again

* Thu Sep 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-07 01:28:44 (60448)
- bump release

* Thu Sep 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-07 01:27:29 (60447)
- Fix buildrequires

* Thu Sep 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-07 01:00:30 (60442)
- Fix buildrequires

* Wed Sep 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-06 22:29:46 (60429)
- initial package

