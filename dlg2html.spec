Summary: Convert DLG Pro BBS message bases to HTML
Name: dlg2html
Version: 1.0
Release: 1
License: GPL
Group: Applications/Text
URL: http://www.nothingisreal.com/dlg2html/
Source0: http://www.nothingisreal.com/dlg2html/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}
Requires: bash, coreutils, sed, grep
Distribution: SuSE 9.0 (noarch)

%description
eoconv is a tool which converts text files to and from the following
Esperanto text encodings:

  * ASCII postfix h notation
  * ASCII postfix x notation
  * ASCII postfix caret (^) notation
  * ASCII prefix caret (^) notation
  * ISO-8859-3
  * Unicode (UTF-7, UTF-8, UTF-16, UTF-32)
  * HTML entities (decimal or hexadecimal)

%prep
%setup -q

%build

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
install -D dlg2html $RPM_BUILD_ROOT%{_prefix}/bin/dlg2html
install -D dlgsplit $RPM_BUILD_ROOT%{_prefix}/bin/dlgsplit

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_prefix}/bin/dlg2html
%{_prefix}/bin/dlgsplit
%doc AUTHORS COPYING NEWS README

%changelog
* Fri Dec  4 2004 Tristan Miller <psychonaut@nothingisreal.com> - 
- Initial build.
