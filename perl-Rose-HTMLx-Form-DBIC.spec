#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Rose
%define	pnam	HTMLx-Form-DBIC
Summary:	Rose::HTMLx::Form::DBIC - Module abstract (<= 44 characters) goes here
#Summary(pl.UTF-8):
Name:		perl-Rose-HTMLx-Form-DBIC
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Rose/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7241fc2f74df00e5f32fb7d997bb227f
URL:		http://search.cpan.org/dist/Rose-HTMLx-Form-DBIC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Rose::HTML::Object) >= 0.600
BuildRequires:	perl(Rose::Object) >= 0.85
BuildRequires:	perl-DBIx-Class-ResultSet-RecursiveUpdate
BuildRequires:	perl-Moose
BuildRequires:	perl-SQL-Translator-DBIx-Class
BuildRequires:	perl-String-Random
BuildRequires:	perl-Template-Toolkit
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports functions integrating Rose::HTML::Form with
DBIx::Class.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Rose/HTMLx/Form/*.pm
%{perl_vendorlib}/Rose/HTMLx/Form/DBIC
%{_mandir}/man3/*
