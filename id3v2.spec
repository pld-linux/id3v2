Summary:	An MP3 technical info viewer and ID3 tag editor
Summary(pl):	Przegl�darka informacji technicznych MP3 i edytor tag�w ID3
Name:		id3v2
Version:	0.1.10
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/id3v2/%{name}-%{version}.tar.gz
# Source0-md5:	a4a5130e49b6451ced32e208a2f9aeab
Patch0:		%{name}-DESTDIR.patch
URL:		http://id3v2.sourceforge.net/
BuildRequires:	id3lib-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ID3 tags can be found on mp3 files, they can store infomation about
what band recorded the song, the song name, etc. id3v2 adds all kinds
of neat stuff.

%description -l pl
Tagi ID3 mog� by� znalezione w plikach mp3, mog� zawiera� informacje o
rodzaju muzyki w piosence, nazwie piosenki itp. id3v2 dodaje wszystkie
rodzaje tego typu danych.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	PREFIX="%{_prefix}"
	CPP="%{__cxx}" \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -DVERSION=\\\"%{version}\\\"" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	CPP="%{__cxx}" \
	LDFLAGS="%{rpmldflags}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
