class DragEventState {
  final double dx;
  final double dy;

  DragEventState(this.dx, this.dy);
}

import 'package:flutter_bloc/flutter_bloc.dart';

class DragEventBloc extends Cubit<DragEventState> {
  DragEventBloc() : super(DragEventState(0, 0));

  void updatePosition(double dx, double dy) {
    emit(DragEventState(dx, dy));
  }
}

void main() {
  runApp(
    BlocProvider(
      create: (context) => DragEventBloc(),
      child: MyApp(),
    ),
  );
}

GestureDetector(
  onPanUpdate: (details) {
    BlocProvider.of<DragEventBloc>(context)
        .updatePosition(details.localPosition.dx, details.localPosition.dy);
  },
  child: // Your draggable widget here
)

BlocBuilder<DragEventBloc, DragEventState>(
  builder: (context, state) {
    // Use state.dx and state.dy as needed
    return Text("Position: (${state.dx}, ${state.dy})");
  },
)