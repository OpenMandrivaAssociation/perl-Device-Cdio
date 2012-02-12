%define module	Device-Cdio

Name:		perl-%{module}
Version:	0.3.0
Release:	1
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
