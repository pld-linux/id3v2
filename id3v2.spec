Summary:	An MP3 technical info viewer and ID3 tag editor
Summary(pl.UTF-8):	Przeglądarka informacji technicznych MP3 i edytor tagów ID3
Name:		id3v2
Version:	0.1.11
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/id3v2/%{name}-%{version}.tar.gz
# Source0-md5:	68afc3827cf01501dfb22949f901f1d8
Patch0:		%{name}-DESTDIR.patch
URL:		http://id3v2.sourceforge.net/
BuildRequires:	id3lib-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ID3 tags can be found on MP3 files, they can store infomation about
what band recorded the song, the song name, etc. id3v2 adds all kinds
of neat stuff.

%description -l pl.UTF-8
Tagi ID3 mogą być znalezione w plikach MP3, mogą zawierać informacje o
rodzaju muzyki w piosence, nazwie piosenki itp. id3v2 dodaje wszystkie
rodzaje tego typu danych.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	PREFIX="%{_prefix}" \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -DVERSION=\\\"%{version}\\\"" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
