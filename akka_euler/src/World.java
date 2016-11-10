package akka_euler;

import akka.actor.Props;
import akka.actor.UntypedActor;
import akka.actor.ActorRef;

/**
 * This class creates counters and sums their sums
 */
public class World extends UntypedActor {

    private static double sum = 0.0;
    private static Integer actorsLeft = Config.ACTOR_COUNT;

    /**
     * Calculate the sum.
     * Each counter sums the number from its own partion, so this sums everything.
     */
    public void onReceive(Object msg) {
        if (msg != null) {
            sum += (int) msg;
            actorsLeft--;
            if (actorsLeft <= 0) {
                System.out.println(sum);
                getContext().stop(getSelf());
            }
        } else {
            unhandled(msg);
        }
    }

    /**
     * Initializes a number of actors (ACTOR_COUNT)
     */
    @Override
    public void preStart() {
        for (int i = 0; i < Config.ACTOR_COUNT; i++) {
            final ActorRef counter = getContext().actorOf(
                            Props.create(Counter.class),
                            "counter" + Integer.toString(i));
            // pass the range to the counters (range doesn't include the LIMIT)
            Range range = new Range(i*(Config.LIMIT/Config.ACTOR_COUNT), (Config.LIMIT/Config.ACTOR_COUNT));
            counter.tell(range, getSelf());
        }
    }
}