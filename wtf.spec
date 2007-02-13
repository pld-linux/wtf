Summary:	Translates acronyms for you
Summary(pl.UTF-8):	Tłumaczenie znaczenia akronimów
Name:		wtf
Version:	20051104
Release:	1
License:	Public domain
Group:		Applications/Games
Source0:	http://www.mu.org/~mux/wtf/%{name}-%{version}.tar.gz
# Source0-md5:	93ca90bef86d2f58da14ed0db87cbf78
Patch0:		%{name}-updates.patch
Patch1:		%{name}-man.patch
Requires:	grep
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Translates acronyms for you.

%description -l pl.UTF-8
Program do tłumaczenia znaczenia akronimów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/misc,%{_mandir}/man6}

install acronyms* $RPM_BUILD_ROOT%{_datadir}/misc
install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/misc/acronyms*
