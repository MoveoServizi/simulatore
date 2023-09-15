
(cl:in-package :asdf)

(defsystem "simulator-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "cluster" :depends-on ("_package_cluster"))
    (:file "_package_cluster" :depends-on ("_package"))
    (:file "event" :depends-on ("_package_event"))
    (:file "_package_event" :depends-on ("_package"))
    (:file "loginfo" :depends-on ("_package_loginfo"))
    (:file "_package_loginfo" :depends-on ("_package"))
  ))