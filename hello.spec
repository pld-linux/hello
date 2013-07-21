Summary:	Hello, world!
Summary(pl.UTF-8):	Witaj świecie!
Name:		hello
Version:	2.8
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://ftp.gnu.org/gnu/hello/%{name}-%{version}.tar.gz
# Source0-md5:	6a67cbbbc0420061ef938a9a2736fbd6
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/hello/hello.html
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.18.1
BuildRequires:	help2man
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 'hello' command is for printing a greeting message.

%description -l pl.UTF-8
Polecenie 'hello' służy do wyświetlania niezobowiązującego
pozdrowienia.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/hello
%{_mandir}/man1/hello.1*
%{_infodir}/hello.info*
