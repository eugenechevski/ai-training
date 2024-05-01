import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

// Events
abstract class PositionEvent {}

class PositionUpdated extends PositionEvent {
  final Offset position;
  PositionUpdated(this.position);
}

// States
abstract class PositionState {}

class PositionInitial extends PositionState {}

class PositionChanged extends PositionState {
  final Offset position;
  PositionChanged(this.position);
}

// Bloc
class PositionBloc extends Bloc<PositionEvent, PositionState> {
  PositionBloc() : super(PositionInitial()) {
    on<PositionUpdated>((event, emit) {
      emit(PositionChanged(event.position));
    });
  }
}


// Source Widget (Draggable Item)
class DraggableItem extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Draggable(
      feedback: Container(
        width: 100,
        height: 100,
        color: Colors.blue,
      ),
      childWhenDragging: Container(
        width: 100,
        height: 100,
        color: Colors.blue.withOpacity(0.5),
      ),
      onDragEnd: (details) {
        // Dispatch the PositionUpdated event
        context.read<PositionBloc>().add(PositionUpdated(details.offset));
      },
      child: Container(
        width: 100,
        height: 100,
        color: Colors.blue,
        child: Center(child: Text('Drag Me')),
      ),
    );
  }
}

// Target Widget (Displays Position)
class PositionDisplay extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocBuilder<PositionBloc, PositionState>(
      builder: (context, state) {
        if (state is PositionChanged) {
          return Text('X: ${state.position.dx}, Y: ${state.position.dy}');
        } else {
          return Text('Drag the item');
        }
      },
    );
  }
}