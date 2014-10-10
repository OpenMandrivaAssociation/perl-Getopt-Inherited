%define upstream_name    Getopt-Inherited
%define upstream_version 1.100860

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Handling inherited command-line options
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Getopt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::Accessor::Complex)
BuildRequires:	perl(Class::Accessor::Installer)
BuildRequires:	perl(Data::Inherited)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
By subclassing this mixin class, your program gets the ability to inherit
command-line option specifications. If you have several programs that share
common code and common command-line options you don't want to have to write
the command-line processing code again and again. Using this class you can
abstract command-line options shared by your programs into a superclass
from which your programs then inherit. Additionally, this class defines
certain common command-line options itself.

You can also define defaults for command-line options.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.100.860-2mdv2011.0
+ Revision: 654194
- rebuild for updated spec-helper

* Sun Mar 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.860-1mdv2011.0
+ Revision: 528432
- update to 1.100860

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.1
+ Revision: 502083
- import perl-Getopt-Inherited


* Mon Feb 08 2010 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist
