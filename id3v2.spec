Summary:	A command line id3v2 tag editor.
Summary(pl):	Program wiersza polecen do tagów id3v2.
Name:		id3v2
Version:	0.1.9
Release:	1
Epoch:		1
License:	GPL
Group:		-
Vendor:		-
Source0:	%{name}-%{version}.tar.gz
URL:		http://id3v2.sourceforge.net/
BuildRequires:	id3lib-devel
Requires:	id3lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
