#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log 
%define	pnam	Channel
Summary:	Log::Channel - yet another logging package
Summary(pl):	Log::Channel - jeszcze jeden pakiet do logowania
Name:		perl-Log-Channel
Version:	0.6
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0a60ac326603e73da44d11bd82ecaa62
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Log-Dispatch
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Log::Channel Perl module allows for code to specify channels for
delivery of logging messages, and for users of the code to control the
delivery and formatting of the messages.

%description -l pl
Modu³ Perla Log::Channel umo¿liwia okre¶lenie w kodzie kana³ów
logowania komunikatów. Umo¿liwia te¿ u¿ytkownikom kodu sterowanie
dorêczaniem i formatowaniem komunikatów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
