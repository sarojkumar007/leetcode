type Callback = (...args: any[]) => any;
type Subscription = {
  unsubscribe: () => void;
};

class EventEmitter {
  eventMap: { [e: string]: Set<Callback> } = {}; // 'event' => Set()

  subscribe(eventName: string, callback: Callback): Subscription {
    if (!this.eventMap[eventName]) this.eventMap[eventName] = new Set();
    this.eventMap[eventName].add(callback);

    return {
      unsubscribe: () => {
        this.eventMap[eventName].delete(callback);
      },
    };
  }

  emit(eventName: string, args: any[] = []): any[] {
    const res: any[] = [];

    // forEach :: on event, if exists otherwise on []
    (this.eventMap[eventName] ?? []).forEach((cb) => res.push(cb(...args)));
    return res;
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
