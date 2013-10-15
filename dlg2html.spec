Summary: Convert DLG Pro BBS message bases to HTML
Name: dlg2html
Version: 1.1
Release: 1
License: GPL
Group: Applications/Text
URL: http://www.nothingisreal.com/dlg2html/
Source0: http://www.nothingisreal.com/dlg2html/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}
Requires: bash, coreutils, sed, grep
Distribution: SuSE 11.4 (noarch)
BuildArch: noarch

%description
dlg2html is a set of Bash shell scripts which help automate the
conversion of DLG Pro message bases to HTML for archiving or mirroring
on the Web. (DLG Pro is a bulletin board system, or BBS, for Amiga
personal computers.) The HTML message files contain the appropriate
links to the next and previous messages, as well as to any replies or
referenced messages; a message index is also produced. dlg2html works
with terminal dumps of DLG message boards, which means you do not need
access to the actual BBS files to perform the conversion.

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
%doc AUTHORS COPYING NEWS README example.txt

%changelog
* Sun Oct 13 2013 Tristan Miller <psychonaut@nothingisreal.com> - 
- Initial build.
