#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Log
%define		pnam	Channel
Summary:	Log::Channel - yet another logging package
Summary(pl.UTF-8):	Log::Channel - jeszcze jeden pakiet do logowania
Name:		perl-Log-Channel
Version:	0.7
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	744b5f964c5c420395b5c289565498c5
URL:		http://search.cpan.org/dist/Log-Channel/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Log-Dispatch
BuildRequires:	perl-Log-Dispatch-Config
BuildRequires:	perl-XML-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Log::Channel Perl module allows for code to specify channels for
delivery of logging messages, and for users of the code to control the
delivery and formatting of the messages.

%description -l pl.UTF-8
Moduł Perla Log::Channel umożliwia określenie w kodzie kanałów
logowania komunikatów. Umożliwia też użytkownikom kodu sterowanie
doręczaniem i formatowaniem komunikatów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Log/*
%{_mandir}/man3/*
