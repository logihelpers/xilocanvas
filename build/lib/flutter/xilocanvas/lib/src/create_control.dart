import 'package:flet/flet.dart';

import 'xilocanvas.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "xilocanvas":
      return XilocanvasControl(
        parent: args.parent,
        control: args.control,
        children: args.children,
        parentDisabled: args.parentDisabled,
        parentAdaptive: args.parentAdaptive,
        backend: args.backend,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
